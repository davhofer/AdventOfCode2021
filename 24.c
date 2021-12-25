#include <stdio.h>

int A[14] = {12, 13, 12, -13, 11, 15, -14, 12, -8, 14, -9, -11, -6, -5};
int B[14] = {1, 1, 1, 26, 1, 1, 26, 1, 26, 1, 26, 26, 26, 26};
int C[14] = {1, 9, 11, 6, 6, 13, 13, 5, 7, 2, 10, 14, 7, 1};

// built out of B. a z value greater than or equal to this can't possibly reach 0 by the end
long long max_z[14] = {8031810176,8031810176,8031810176,8031810176,308915776,308915776,308915776,11881376,11881376,456976,456976,17576,676,26};

long long stage(int n, int w, long long z)
{
  if (z % 26 + A[n] == w) {
    return z / B[n];
  } else {
    return 26 * (z / B[n]) + w + C[n];
  }
}

int search(int depth, long long z, char solution[15])
{
    if (depth == 14) {
        if (z == 0) {
            solution[depth] = '\0';
            printf("%s\n", solution);
	    return 1;
        }
        return 0;
    }
    else if (z >= max_z[depth])
        return 0;

    for(int i = 1; i <= 9; ++i) {
        solution[depth] = '0' + i;
        if (search(depth + 1, stage(depth, i, z), solution)) {
	    return 1;
	}
    }
}

int main(int argc, char **argv)
{
    char solution[15];
    search(0, 0, solution);
}
