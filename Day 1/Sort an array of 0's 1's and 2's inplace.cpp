#include <iostream>
#include<bits/stdc++.h>
using namespace std;
void sortinPlace(vector<int>& a)
{
	int low=0;
	int mid = 0;
	int high = a.size()-1;
	while(mid <= high)
	{
		if(a[mid] == 0)
		{
			swap(a[mid], a[low]);
			mid++;
			low++;
		}
		else if(a[mid] == 1)
		{
			mid++;
		}
		else if(a[mid] == 2)
		{
			swap(a[mid], a[high]);
			high--;
		}
	}
}
int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int input;
	vector<int> nums;
	while(cin >> input)
	{
		nums.push_back(input);
	}
	sortinPlace(nums);
	for(int i: nums)
	{
		cout << i << " ";
	}
	return 0;
}