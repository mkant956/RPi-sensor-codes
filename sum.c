#include <stdio.h>

int main()
{
	int count, x=0, y=0, varx, vary;
	count = 467;
	int maxx=-100000,minx=10000000,miny=10000000,maxy=-10000000;
	while(count>=0)
	{
		count--;
		scanf("%d", &varx);
		scanf("%d", &vary);
		x = x+varx;
		y = y+vary;
		if(minx>varx)
			minx=varx;
		if(maxx<varx)
			maxx=varx;
		if(miny>vary)
			miny=vary;
		if(maxy<vary)
			maxy=vary;
	}
	printf("avge x = %d  ", x/count);
	printf("avge y = %d\n %d %d %d %d\n", y/count,minx,maxx,miny,maxy);
	
	return 0;

}
