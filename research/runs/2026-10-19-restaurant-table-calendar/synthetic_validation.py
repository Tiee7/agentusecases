"""Local synthetic checks only; does not execute Muse or contact a restaurant."""
import json
from pathlib import Path
from datetime import datetime,timezone

def acceptable(x):
    required={'time','budget','subtotal','tax','tip','confirmed','confirmation','existing_booking'}
    if required-set(x):return False
    try: dt=datetime.fromisoformat(x['time'])
    except (TypeError,ValueError):return False
    if dt.tzinfo is None:return False
    numbers=[x[k] for k in ('budget','subtotal','tax','tip')]
    if any(isinstance(v,bool) or not isinstance(v,(int,float)) or v<0 for v in numbers):return False
    if x['subtotal']+x['tax']+x['tip']>x['budget']:return False
    return x['confirmed'] is True and bool(x['confirmation']) and not x['existing_booking']

def run():
    fixture=dict(time='2026-11-01T18:00:00-05:00',budget=100,subtotal=70,tax=7,tip=14,confirmed=True,confirmation='SYNTHETIC-NOT-A-REAL-RESERVATION',existing_booking=False)
    tests=[]
    for label,changes,expected in [
        ('complete synthetic record passes',{},True),
        ('menu cost above stated budget rejected',{'subtotal':110},False),
        ('tax and tip can make affordable menu exceed all-in budget',{'subtotal':90},False),
        ('unconfirmed request cannot be called booked',{'confirmed':False},False),
        ('missing confirmation rejected',{'confirmation':''},False),
        ('existing reservation must not be resubmitted',{'existing_booking':True},False),
        ('naive local time rejected',{'time':'2026-11-01T18:00:00'},False),
        ('unknown tax cannot be treated as zero',{'tax':None},False),
        ('negative cost rejected',{'tip':-1},False),
    ]:
        actual=acceptable(dict(fixture,**changes));assert actual==expected,label
        tests.append(dict(check=label,passed=True))
    models=json.load(open('research/book-a-restaurant-table-and-add-it-to-the-calendar.json'))['unit_economics']
    calculations=[]
    for m in models:
        variable=sum(m[k] for k in ('api_cost','human_cost','other_variable_cost','acquisition_cost'))
        contribution=m['price']-variable;profit=contribution*m['units_per_month']-m['fixed_monthly_cost']
        cash=m['units_per_month']*(m['api_cost']+m['other_variable_cost']+m['acquisition_cost'])+m['fixed_monthly_cost']
        calculations.append(dict(scenario=m['scenario'],variable=variable,contribution=contribution,monthly_contribution=profit,cash_4weeks=cash,extra_channel_fee_effect=f'minus volume*x ({m["units_per_month"]}*x)'))
    assert abs(calculations[0]['monthly_contribution']-53.33333333333333)<1e-8
    assert calculations[1]['monthly_contribution']==-100
    assert calculations[0]['cash_4weeks']==120 and calculations[1]['cash_4weeks']==145
    max_minutes=(12-.5-.5-4-20/20)*60/25;assert abs(max_minutes-14.4)<1e-8
    result=dict(scope='Synthetic Python checks of researcher-proposed acceptance rules and arithmetic. No model execution, login, real reservation, cancellation, payment, API call, or restaurant contact.',tested_at=datetime.now(timezone.utc).isoformat(),checks=tests,calculations=calculations,maximum_break_even_human_minutes=max_minutes,agent_reliability_measured=False)
    p=Path(__file__).with_name('synthetic-results.json');p.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n');print(json.dumps(result,ensure_ascii=False,indent=2))
if __name__=='__main__':run()
