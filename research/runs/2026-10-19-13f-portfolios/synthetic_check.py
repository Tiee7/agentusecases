import json
def compare(prev,current):
 def normalize(rows):
  out={}
  for x in rows:
   key=(x['id'],x['type'])
   if key in out:raise ValueError('duplicate')
   if x['unit'] not in ('USD','USD_thousands'):raise ValueError('unknown unit')
   if x.get('amendment_unresolved'):raise ValueError('unresolved amendment')
   out[key]={'shares':x['shares'],'value':x['value']*(1000 if x['unit']=='USD_thousands' else 1)}
  return out
 p,c=normalize(prev),normalize(current)
 return {str(k):{'share_change':c[k]['shares']-p[k]['shares'] if k in p and k in c else None,'value_change':c[k]['value']-p[k]['value'] if k in p and k in c else None,'status':'matched' if k in p and k in c else 'not_seen_in_one_table'} for k in p.keys()|c.keys()}
def row(i='A',t='common',s=10,v=100,u='USD',**kw):return dict(id=i,type=t,shares=s,value=v,unit=u,**kw)
checks=[]
r=compare([row()],[row(v=120)]);assert r["('A', 'common')"]['share_change']==0;checks.append('price_change_not_share_purchase')
r=compare([row(v=1,u='USD_thousands')],[row(v=1000)]);assert r["('A', 'common')"]['value_change']==0;checks.append('explicit_unit_normalization')
r=compare([row()],[row(t='put')]);assert len(r)==2 and all(x['share_change'] is None for x in r.values());checks.append('types_not_merged')
r=compare([row()],[]);assert r["('A', 'common')"]['share_change'] is None;checks.append('absence_not_invented_zero_sale')
for name,rows in [('duplicate',[row(),row()]),('unknown unit',[row(u='unknown')]),('unresolved amendment',[row(amendment_unresolved=True)])]:
 try:compare([],rows);raise AssertionError(name)
 except ValueError:checks.append(name)
print(json.dumps({'passed':len(checks),'checks':checks,'scope':'Restricted synthetic normalization checks, not upstream Finance code execution or actual institutional holdings analysis.'},indent=2))

