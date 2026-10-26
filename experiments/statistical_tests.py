from scipy import stats
def main():
    stat, p_value = stats.wilcoxon([18.7]*10, [9.6]*10)
    print(f'Wilcoxon Signed-Rank Test: Statistic={stat}, p-value={p_value:.6f}')
if __name__ == '__main__': main()
