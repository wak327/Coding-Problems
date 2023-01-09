#include <iostream>
using namespace std;


void solve()
{
	int a=0,b=0;
	int c;
	for(int i=0; i<5;i++)
	{
		for(int j=0;j<5;j++)
		{
			cin>>c;
			if(c==1){
				a=i;
				b=j;
			}
		}
	}
	cout<<abs(a-2)+abs(b-2);
}

int main()
{
	solve();
	return 0;
}