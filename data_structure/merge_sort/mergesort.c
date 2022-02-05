#include <stdio.h>

#define MAX_SIZE 10
int sorted[MAX_SIZE];
void merge_sort(int list[], int left, int right);
void merge(int list[], int left, int mid, int right);

int main()
{
    int i;
    int list[MAX_SIZE] = {52, 14, 3, 56, 32, 76, 19, 90, 15, 53};
    merge_sort(list, 0, 7);
    for (i = 0; i < MAX_SIZE; i++)
    {
        printf("%d\n", list[i]);
    }
    return 0;
}
void merge_sort(int list[], int left, int right)
{
    int mid;
    if (left < right)
    {
        mid = (left + right) / 2;
        merge_sort(list, left, mid);
        merge_sort(list, mid + 1, right);
        merge(list, left, mid, right); //? •? ¬?œ ?‘ê°œì˜ ë°°ì—´ ?•©ë³?
    }
    else
        return;
}
void merge(int list[], int left, int mid, int right)
{
    int i, j, k, l;
    i = left;
    k = left;
    j = mid + 1;
    while (i <= mid && j <= right)
    {
        if (list[i] <= list[j])
            sorted[k++] = list[i++];
        else
            sorted[k++] = list[j++];
    }
    if (i > mid) // mid?™¼ìª½ì?? ?‹¤ ì±„ì›Œ?„£??? ê²½ìš° ?‚˜ë¨¸ì???Š” mid?˜¤ë¥¸ìª½?—?„œ ?‹¤ ë³µì‚¬?•´?„œ sortedë°°ì—´?— ?„£?œ¼ë©´ë¨
        for (l = j; l <= right; l++)
            sorted[k++] = list[l];
    else
        for (l = i; l <= mid; l++)
            sorted[k++] = list[l];
    for (l = left; l <= right; l++)
    {
        list[l] = sorted[l];
    }
}
