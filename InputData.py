# simulation settings
POP_SIZE = 4287     # We used 1% of 428724 - the target population size - the total number of people >50yrs of age living with HIV in USA - source: https://www.cdc.gov/hiv/group/age/olderamericans/index.html
#limitation - we'd have liked to simulate all 428724 people in the target population, but it broke python down because it was too large of a simulation
#additional limitation - we have the discount rate, but aren't necessarily able to account for the aging population of people living with HIV as ART improves and keeps them alive longer.
SIM_LENGTH = 100    # length of simulation (years)
ALPHA = 0.05        # significance level for calculating confidence intervals
DISCOUNT = 0.03     # annual discount rate

ADD_BACKGROUND_MORT = True  # if background mortality should be added
DELTA_T = 1/4       # years

PSA_ON = True      # if probabilistic sensitivity analysis is on

# transition matrix - edit data here
TRANS_MATRIX = [
    [3093,  864,    287,    42],   # Healthy with HIV
    [0,     1807,    1265,    37],   # HIV+ and experienced cardiac event
    [0,     0,      3216,   1071],  # severe cardiac event
    ]



# annual cost of each health state
ANNUAL_STATE_COST = [
    34316.0,   # Healthy with HIV - Annual medical cost estimates for HIV-infected persons, adjusted for age, sex, race/ethnicity, and transmission risk group, were from the HIV Research Network (range $1,854–$4,545/month). We took the average - $3618 - and multiplied by 12 months for $43416 - source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4359630/
    37892.6,   # HIV+ and experienced cardiac event - for patients with Medicaid, this is an incremental $4959 additional cost. For those with other insurance than Medicaid, there is an incremental $2655 cost. Because about 40% of people with HIV use Medicaid, we solved for this cost as follows (.6*2655+.4*4959)
    77679.83    # Severe, fatal cardiac event - data shows this costs 1.2-2.9 times more than a nonfatal cardiac event. We took the average and multipled the cost of a cardiac event above by 2.05. source: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4467662/
    ]
#Source for data on cost:  https://www.ncbi.nlm.nih.gov/pubmed/28933204 - limitation: didn't account for fact that cost for elderly patients may be higher
#Source for data on HIV pop with Medicaid as insurance: https://www.kff.org/hivaids/fact-sheet/medicaid-and-hiv/
#Limitation: We did not account for people who are uninsured in this study, which are a sizable portion of the HIV+ population, because cost data was not available for them.
#Limitation - an HIV-specific data source was not available for cardiac deaths, so we made assumptions based on data on the general population. Given the complexities of HIV and expense of care, this may be skewed toward a lower cost.


# annual health utility of each health state
ANNUAL_STATE_UTILITY = [
    0.9,   # HIV+
    0.8,   # HIV+ and experience cardiac event
    0.0001   # Death from cardiac event
    ]

# annual cost of therapy versus untreated
Nointervention_COST = 0
OTCStatin_COST = 305.04 #Data on annual cost of over the counter statin medication, from cost-effectiveness study and IMS data, source: http://www.ajmc.com/journals/issue/2016/2016-vol22-n5/a-cost-effectiveness-analysis-of-over-the-counter-statins

# treatment relative risk
TREATMENT_RR = 0.78           # relative risk of cardiac disease mortality with statins - source: https://www.ncbi.nlm.nih.gov/pubmed/14692706
TREATMENT_RR_CI = 0.73, 0.84  # relative risk of cardiac disease mortality with statins, lower 95% CI, upper 95% CI - source: https://www.ncbi.nlm.nih.gov/pubmed/14692706
#limitation - data is not yet available for the relative risk of cardiac disease mortality with statins on people living with HIV - researchers suspect the outcomes will be as positive or even more positive because statins have already been shown in smaller studies to reduce the size of cardiac plaques that often contribute to cardiac events substantially
# update annual probability of background mortality (number per year per 1,000 population)
ANNUAL_PROB_BACKGROUND_MORT = 118 / 10000 # source - https://www.thelancet.com/pdfs/journals/lanpub/PIIS2468-2667(16)30020-2.pdf
