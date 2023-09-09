#include "lists.h"

/**
 * reverse_list - reverses a listint_t linked list.
 * @head: a pointer to the head of the linked list.
 *
 * Return: a pointer to the first node of the reversed list.
 */
listint_t *reverse_list(listint_t *head)
{
	listint_t *current, *prev = NULL;

	while (current != NULL)
	{
		current = head->next;
		head->next = prev;
		prev = head;
		head = current;
	}

	return (prev);
}

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: a double pointer to the head of the linked list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *slow, *fast, *middle_node;

	slow = fast = *head;

	if (*head == NULL || head == NULL)
		return (1);

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
	}

	middle_node = reverse_list(slow);

	while (middle_node != NULL)
	{
		if ((*head)->n != middle_node->n)
			return (0);
		*head = (*head)->next;
		middle_node = middle_node->next;
	}

	return (1);
}
