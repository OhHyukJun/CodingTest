#include <iostream>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> nums) {
	set<int> tmp1;
	for (const auto& num : nums)
		tmp1.insert(num);
	return min(nums.size() / 2, tmp1.size());
}