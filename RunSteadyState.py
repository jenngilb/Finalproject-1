import SurvivalModelClasses as Cls
import scr.SamplePathClasses as SamplePathSupport
import scr.FigureSupport as Fig

MORTALITY_PROB = 0.1    # annual probability of mortality
TIME_STEPS = 100        # simulation length
SIM_POP_SIZE = 1000     # population size of the simulated cohort
ALPHA = 0.05            # significance level

# create a cohort of patients
myCohort = Cls.Cohort(id=1, pop_size=SIM_POP_SIZE, mortality_prob=MORTALITY_PROB)

# simulate the cohort
cohortOutcome = myCohort.simulate(TIME_STEPS)

# plot the sample path
SamplePathSupport.graph_sample_path(
    sample_path=cohortOutcome.get_survival_curve(),
    title='Survival Curve',
    x_label='Time-Step (Year)',
    y_label='Number Survived')

# plot the histogram
Fig.graph_histogram(
    data=myCohort.get_survival_times(),
    title='Histogram of Patient Survival Time',
    x_label='Survival Time (Year)',
    y_label='Count')

# print the patient survival time
print('Average survival time (years):', cohortOutcome.get_ave_survival_time())
print('95% CI of average survival time (years)', cohortOutcome.get_CI_survival_time(ALPHA))
