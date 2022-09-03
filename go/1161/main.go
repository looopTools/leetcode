package main



type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func findMaxLevel(levelSumMap map[int]int) int {

	level := 0;
	sum := 0;

	for key, value := range levelSumMap {

		if sum == 0 || sum < value {
			level = key;
			sum = value
		}
	}

	return level;
}

func visitNode(node *TreeNode, level int, levelSumMap *map[int]int) {

	levelSum, exists :=  (*levelSumMap)[level];

	if exists {
		(*levelSumMap)[level] = levelSum + node.Val;
	} else {
		(*levelSumMap)[level] = node.Val;
	}
	
	
	if node.Left != nil {
		visitNode(node.Left, level + 1, levelSumMap);
	}

	if node.Right != nil {
		visitNode(node.Right, level + 1, levelSumMap);
	}
}

func maxLevelSum(root *TreeNode) int {

	levelSumMap := make(map[int]int);
	visitNode(root, 1, &levelSumMap);
	return findMaxLevel(levelSumMap)
}



