import SurvivalModelClasses as Cls
import scr.FigureSupport as Fig

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
REAL_POP_SIZE = 100     # size of the real cohort to make the projections for
NUM_SIM_COHORTS = 1000   # number of simulated cohorts used for making projections
ALPHA = 0.05            # significance level

# calculating prediction interval for mean survival time
# create multiple cohorts
multiCohort = Cls.MultiCohort(
    ids=range(NUM_SIM_COHORTS),   # [0, 1, 2 ..., NUM_SIM_COHORTS-1]
    pop_sizes=[REAL_POP_SIZE] * NUM_SIM_COHORTS,  # [REAL_POP_SIZE, REAL_POP_SIZE, ..., REAL_POP_SIZE]
    mortality_probs=[MORTALITY_PROB]*NUM_SIM_COHORTS  # [p, p, ....]
)
# simulate all cohorts
multiCohort.simulate(TIME_STEPS)

# plot the histogram of average survival time
Fig.graph_histogram(
    data=multiCohort.get_all_mean_survival(),
    title='Histogram of Mean Survival Time',
    x_label='Mean Survival Time (Year)',
    y_label='Count')

# print projected mean survival time (years)
print('Projected mean survival time (years)',
      multiCohort.get_overall_mean_survival())
# print projection interval
print('95% projection interval of average survival time (years)',
      multiCohort.get_PI_mean_survival(ALPHA))
