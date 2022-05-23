#include<stdio.h>

int main() {

	int N, K;
	int c[1000] = {0,};
	scanf_s("%d %d", &N, &K);
	int min=1000;
	int count = 0;
	for (int i = 2; i <= N; i++)
	{
		c[i] = i;

	}

	
	for (int i = 2; i <= N; i++)
	{
		if (c[i] <= 0)
		{
			continue;
		}
		else
		{
			for (int j = i; j <= N; j+=i)
			{
				if (c[j] != 0)
				{
					c[j] = 0;
					count++;
				}

				if (count == K) {
					printf("%d", j);
					break;
				}
			}
		}
	}

}
