def prune(tree, miniGain, evaluationFunction=gini):
    # quand gain < mini Gain，fusioner  trueBranch et la  the falseBranch

    if tree.trueBranch.results == None: prune(tree.trueBranch, miniGain, evaluationFunction)
    if tree.falseBranch.results == None: prune(tree.falseBranch, miniGain, evaluationFunction)

    if tree.trueBranch.results != None and tree.falseBranch.results != None:
        len1 = len(tree.trueBranch.data)
        len2 = len(tree.falseBranc  h.data)
        len3 = len(tree.trueBranch.data + tree.falseBranch.data)
        p = float(len1) / (len1 + len2)
        gain = evaluationFunction(tree.trueBranch.data + tree.falseBranch.data) - p * evaluationFunction(
            tree.trueBranch.data) - (1 - p) * evaluationFunction(tree.falseBranch.data)
        if (gain < miniGain):
            tree.data = tree.trueBranch.data + tree.falseBranch.data
            tree.results = calculateDiffCount(tree.data)
            tree.trueBranch = None
            tree.falseBranch = None

def classify(data, tree):
    if tree.results != None:
        return tree.results
    else:
        branch = None
        v = data[tree.col]
        if isinstance(v, int) or isinstance(v, float):
            if v >= tree.value:
                branch = tree.trueBranch
            else:
                branch = tree.falseBranch
        else:
            if v == tree.value:
                branch = tree.trueBranch
            else:
                branch = tree.falseBranch
        return classify(data, branch)