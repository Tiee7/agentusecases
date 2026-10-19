"""Synthetic calculation checks only; not the unavailable author's application."""
import math,json
from datetime import date
def xirr(values,dates):
 if len(values)!=len(dates) or len(values)<2:raise ValueError('length')
 if not any(v<0 for v in values) or not any(v>0 for v in values):raise ValueError('sign')
 if any(not math.isfinite(v) for v in values):raise ValueError('nonfinite')
 ds=[date.fromisoformat(s) for s in dates]
 if any(d<ds[0] for d in ds):raise ValueError('start')
 if len(set(ds))!=len(ds):raise ValueError('duplicate: review instead of silently merging')
 times=[(d-ds[0]).days/365 for d in ds]
 if max(times)==0:raise ValueError('no duration')
 def f(r):return sum(v/(1+r)**t for v,t in zip(values,times))
 lo,hi=-.99,10
 if f(lo)*f(hi)>0:raise ValueError('no bracket; no invented result')
 for _ in range(200):
  mid=(lo+hi)/2
  if f(lo)*f(mid)<=0:hi=mid
  else:lo=mid
 return (lo+hi)/2
checks=[]
def ck(n,v):assert v,n;checks.append(n)
ck('365-day synthetic 10 percent',abs(xirr([-100,110],['2025-01-01','2026-01-01'])-.1)<1e-10)
ck('730-day synthetic 10 percent',abs(xirr([-100,121],['2025-01-01','2027-01-01'])-.1)<1e-10)
for name,v,ds in [('no positive',[-100,-10],['2025-01-01','2026-01-01']),('bad date',[-100,110],['bad','2026-01-01']),('mismatched length',[-100,110],['2025-01-01']),('duplicate review',[-100,110],['2025-01-01','2025-01-01']),('earlier date',[-100,110],['2026-01-01','2025-01-01'])]:
 try:xirr(v,ds);raise AssertionError(name)
 except ValueError:checks.append(name)
print(json.dumps({'passed':len(checks),'checks':checks,'scope':'Synthetic restricted numerical exercise. Not a general XIRR implementation, not author-code validation, not investment advice.'},indent=2))

