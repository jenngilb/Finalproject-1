import ParameterClasses as P
import MarkovModelClasses as MarkovCls
import SupportMarkovModel as SupportMarkov


# simulating no therapy
# create a cohort
cohort_none = MarkovCls.Cohort(
    id=0,
    therapy=P.Therapies.NONE)
# simulate the cohort
simOutputs_none = cohort_none.simulate()

# simulating statin therapy
# create a cohort
cohort_statin = MarkovCls.Cohort(
    id=1,
    therapy=P.Therapies.STATIN)
# simulate the cohort
simOutputs_statin = cohort_statin.simulate()

# draw survival curves and histograms
SupportMarkov.draw_survival_curves_and_histograms(simOutputs_none, simOutputs_statin)

# print the estimates for the mean survival time and mean time to cardiac death
SupportMarkov.print_outcomes(simOutputs_none, "No Therapy:")
SupportMarkov.print_outcomes(simOutputs_statin, "Statin Therapy:")

# print comparative outcomes
SupportMarkov.print_comparative_outcomes(simOutputs_none, simOutputs_statin)

# report the CEA results
SupportMarkov.report_CEA_CBA(simOutputs_none, simOutputs_statin)

