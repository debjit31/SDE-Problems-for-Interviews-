#include <iostream>
#include<bits/stdc++.h>
using namespace std;
/* Appraoch 1 :- Using a 3rd array*/
int main() {
	
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	
	int input;
	vector<int> a, b;
	while(cin >> input)
	{
		a.push_back(input);
	}
	while(cin >> input)
	{
		b.push_back(input);
	}
	vector<int> c(a.size()+b.size());
	int i=0;
	for(int j=0;j<a.size();j++)
	{
		c[i] = a[j];
		i++;
	}
	for(int t=0;t<b.size();t++)
	{
		c[i] = b[t];
		i++;
	}
	sort(c.begin(), c.end());
	int x;
	for(x=0;x<a.size();x++)
	{
		a[x] = c[x];
	}
	for(int t=x;t<c.size();t++)
	{
		b[x-a.size()] = c[x];
	}
	for(int x : a){
		cout << x << " ";
	}
	cout << "\n";
	for(int x : b){
		cout << x << " ";
	}
	return 0;
}