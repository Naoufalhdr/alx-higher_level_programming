#include "lists.h"
#include <stdio.h>

/**
 * check_cycle - Checks if a linked list has a cycle
 * @list: is the pointer to the head of the linked list
 *
 * Return: 1 if a cycle is detected, 0 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *ptr1, *ptr2;

	if (list == NULL || list->next == NULL)
		return (0);

	ptr1 = ptr2 = list;
	while(ptr2->next != NULL && ptr2->next->next != NULL)
	{
		ptr1 = ptr1->next;
		ptr2 = ptr2->next->next;
		if (ptr1 == ptr2)
			return (1);
	}
	return (0);
}
