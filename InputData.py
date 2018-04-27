
# simulation settings
POP_SIZE = 428724     # The cohort population size is the total number of people >50yrs of age living with HIV in USA - source: https://www.cdc.gov/hiv/group/age/olderamericans/index.html
SIM_LENGTH = 100    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ADD_BACKGROUND_MORT = True  # if background mortality should be added
DELTA_T = 1/4       # years

PSA_ON = True      # if probabilistic sensitivity analysis is on

# transition matrix
TRANS_MATRIX = [
    [1251,  350,    116,    17],   # CD4_200to500
    [0,     731,    512,    15],   # CD4_200
    [0,     0,      1312,   437],   # AIDS
    ]

# annual cost of each health state
ANNUAL_STATE_COST = [
    2756.0,   # CD4_200to500
    3025.0,   # CD4_200
    9007.0    # AIDS
    ]

# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.75,   # CD4_200to500
    0.50,   # CD4_200
    0.25    # AIDS
    ]

# annual cost of therapy versus untreated
Nointervention_COST = 2278.0
OTCStatin_COST = 25.42*12 #Data on annual cost of over the counter statin medication, from cost-effectiveness study and IMS data, source: http://www.ajmc.com/journals/issue/2016/2016-vol22-n5/a-cost-effectiveness-analysis-of-over-the-counter-statins

# treatment relative risk
TREATMENT_RR = 0.509
TREATMENT_RR_CI = 0.365, 0.71  # lower 95% CI, upper 95% CI

# annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 8.15 / 1000
