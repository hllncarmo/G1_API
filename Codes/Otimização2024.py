from pulp import LpMinimize, LpProblem, lpSum, LpVariable, LpStatus

# Define the problem data
plants = [3403208, 3423909, 3424402]  # 3 plants
customers = [2301, 2302, 2303, 2304, 2305, 
             2306, 2307, 2308, 2309, 2310, 
             2311, 2312, 2313, 2314, 2315, 
             2316, 2317, 2318, 2319, 2320, 
             2321, 2322, 2323, 2324, 2325, 
             2326, 2327, 2328, 2329, 2330, 
             2331, 2332, 2333, 2334, 2335, 
             2336, 2337, 2338, 2339, 2340, 
             2341, 2342, 2343, 2344, 2345, 
             2346, 2347, 2348, 2349, 2350, 
             2351]  # 51 customers

transportation_costs = {
    (3403208, 2301): 0.581689889,
    (3403208, 2302): 0.479859,
    (3403208, 2303): 0.440461389,
    (3403208, 2304): 0.456173529,
    (3403208, 2305): 0.492159853,
    (3403208, 2306): 0.544231152,
    (3403208, 2307): 0.531967,
    (3403208, 2308): 0.540897912,
    (3403208, 2309): 0.424910965,
    (3403208, 2310): 0.714332699,
    (3403208, 2311): 0.403713274,
    (3403208, 2312): 0.788882677,
    (3403208, 2313): 0.753914848,
    (3403208, 2314): 0.707153831,
    (3403208, 2315): 0.825211267,
    (3403208, 2316): 0.834051632,
    (3403208, 2317): 0.829567813,
    (3403208, 2318): 0.821042543,
    (3403208, 2319): 0.690594586,
    (3403208, 2320): 0.761210333,
    (3403208, 2321): 0.80649625,
    (3403208, 2322): 0.691370481,
    (3403208, 2323): 0.776785333,
    (3403208, 2324): 0.704948765,
    (3403208, 2325): 0.621799889,
    (3403208, 2326): 0.693433396,
    (3403208, 2327): 0.706295309,
    (3403208, 2328): 0.725456763,
    (3403208, 2329): 0.780871538,
    (3403208, 2330): 0.78952527,
    (3403208, 2331): 0.691823939,
    (3403208, 2332): 0.683192821,
    (3403208, 2333): 0.646552766,
    (3403208, 2334): 0.67760587,
    (3403208, 2335): 0.687003068,
    (3403208, 2336): 999,
    (3403208, 2337): 999,
    (3403208, 2338): 999,
    (3403208, 2339): 0.89047,
    (3403208, 2340): 0.956220721,
    (3403208, 2341): 0.902300672,
    (3403208, 2342): 0.892650771,
    (3403208, 2343): 0.973301747,
    (3403208, 2344): 0.629870511,
    (3403208, 2345): 0.63538812,
    (3403208, 2346): 0.63609,
    (3403208, 2347): 0.424221,
    (3403208, 2348): 0.319796772,
    (3403208, 2349): 0.393239,
    (3403208, 2350): 0.388532513,
    (3403208, 2351): 0.426050139,
    (3423909, 2301): 999,
    (3423909, 2302): 999,
    (3423909, 2303): 999,
    (3423909, 2304): 999,
    (3423909, 2305): 0.384921411,
    (3423909, 2306): 999,
    (3423909, 2307): 999,
    (3423909, 2308): 0.384732184,
    (3423909, 2309): 0.424221,
    (3423909, 2310): 0.332182532,
    (3423909, 2311): 0.384714542,
    (3423909, 2312): 999,
    (3423909, 2313): 999,
    (3423909, 2314): 999,
    (3423909, 2315): 999,
    (3423909, 2316): 999,
    (3423909, 2317): 999,
    (3423909, 2318): 999,
    (3423909, 2319): 999,
    (3423909, 2320): 999,
    (3423909, 2321): 999,
    (3423909, 2322): 999,
    (3423909, 2323): 999,
    (3423909, 2324): 0.3229575,
    (3423909, 2325): 999,
    (3423909, 2326): 0.353531597,
    (3423909, 2327): 0.373844423,
    (3423909, 2328): 0.354898829,
    (3423909, 2329): 0.367891282,
    (3423909, 2330): 0.420241744,
    (3423909, 2331): 0.351685809,
    (3423909, 2332): 0.378249667,
    (3423909, 2333): 0.628467,
    (3423909, 2334): 0.424221,
    (3423909, 2335): 0.424221,
    (3423909, 2336): 0.470995102,
    (3423909, 2337): 0.45372783,
    (3423909, 2338): 0.450193701,
    (3423909, 2339): 0.536394444,
    (3423909, 2340): 0.60808452,
    (3423909, 2341): 0.563565321,
    (3423909, 2342): 0.558621044,
    (3423909, 2343): 0.60713659,
    (3423909, 2344): 999,
    (3423909, 2345): 999,
    (3423909, 2346): 999,
    (3423909, 2347): 0.677435774,
    (3423909, 2348): 0.720155369,
    (3423909, 2349): 0.586379648,
    (3423909, 2350): 0.673478162,
    (3423909, 2351): 0.637836585,
    (3424402, 2301): 0.442990636,
    (3424402, 2302): 0.409496915,
    (3424402, 2303): 0.407212002,
    (3424402, 2304): 0.394700974,
    (3424402, 2305): 0.41995255,
    (3424402, 2306): 0.401843269,
    (3424402, 2307): 0.423066157,
    (3424402, 2308): 0.401565675,
    (3424402, 2309): 0.467243454,
    (3424402, 2310): 0.416016692,
    (3424402, 2311): 0.548170849,
    (3424402, 2312): 999,
    (3424402, 2313): 999,
    (3424402, 2314): 999,
    (3424402, 2315): 999,
    (3424402, 2316): 999,
    (3424402, 2317): 999,
    (3424402, 2318): 999,
    (3424402, 2319): 0.416025571,
    (3424402, 2320): 0.331695,
    (3424402, 2321): 0.331695,
    (3424402, 2322): 0.339176069,
    (3424402, 2323): 0.292731923,
    (3424402, 2324): 0.326926515,
    (3424402, 2325): 0.292731923,
    (3424402, 2326): 0.320362562,
    (3424402, 2327): 0.292731923,
    (3424402, 2328): 0.369156958,
    (3424402, 2329): 0.327056154,
    (3424402, 2330): 0.331695,
    (3424402, 2331): 0.349153,
    (3424402, 2332): 0.315119,
    (3424402, 2333): 0.382879,
    (3424402, 2334): 0.382879,
    (3424402, 2335): 0.342763801,
    (3424402, 2336): 0.719737191,
    (3424402, 2337): 0.699144814,
    (3424402, 2338): 0.693860886,
    (3424402, 2339): 999,
    (3424402, 2340): 999,
    (3424402, 2341): 999,
    (3424402, 2342): 999,
    (3424402, 2343): 999,
    (3424402, 2344): 0.465102596,
    (3424402, 2345): 0.477143788,
    (3424402, 2346): 0.469918289,
    (3424402, 2347): 0.879701638,
    (3424402, 2348): 0.935080972,
    (3424402, 2349): 1.1022266667,
    (3424402, 2350): 1.0105483568,
    (3424402, 2351): 1.1357314706
}

customer_demands = {
    2301:   1860269,
    2302:   361934,
    2303:   1025655,
    2304:   821433,
    2305:   2255987,
    2306:   2476419,
    2307:   5832750,
    2308:   4159584,
    2309:   6708117,
    2310:   1053228,
    2311:   5449152,
    2312:   1226847,
    2313:   6666,
    2314:   56358,
    2315:   3315123,
    2316:   237174,
    2317:   14544,
    2318:   496314,
    2319:   871226,
    2320:   15150,
    2321:   52722,
    2322:   1614990,
    2323:   6515,
    2324:   4705893,
    2325:   32270,
    2326:   3512376,
    2327:   2153876,
    2328:   3656604,
    2329:   2049492,
    2330:   700688,
    2331:   1731948,
    2332:   37269,
    2333:   4697,
    2334:   927938,
    2335:   7103835,
    2336:   1621353,
    2337:   712429,
    2338:   2254926,
    2339:   20907,
    2340:   861202,
    2341:   4809822,
    2342:   705763,
    2343:   7504704,
    2344:   610924,
    2345:   3225587,
    2346:   38481,
    2347:   2316132,
    2348:   962732,
    2349:   10302,
    2350:   3647817,
    2351:   12953,

}

plant_supplies = {
    3403208: 90000000,
    3423909: 56000000,
    3424402: 90000000
}

# Create the linear programming problem
prob = LpProblem("Transportation_Cost_Minimization", LpMinimize)

# Define the decision variables
shipments = LpVariable.dicts("Shipments", (plants, customers), 0, None, cat='Integer')

# Define the objective function
prob += lpSum([transportation_costs[(p, c)] * shipments[p][c] for p in plants for c in customers if (p, c) in transportation_costs])

# Define the constraints
for p in plants:
    prob += lpSum([shipments[p][c] for c in customers]) <= plant_supplies[p]

for c in customers:
    prob += lpSum([shipments[p][c] for p in plants]) == customer_demands[c]



# Solve the problem
prob.solve()

# Print the results
print("Status:", LpStatus[prob.status])
for v in prob.variables():
    print(v.name, "=", v.varValue)