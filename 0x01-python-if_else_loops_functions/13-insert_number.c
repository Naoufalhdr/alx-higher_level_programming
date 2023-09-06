#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - inserts a new node into a sorted singly linked list
 * @head: is the pointer to a pointer to the head of the linked list
 * @number: the value to be inserted into the new node
 *
 * Return: a pointer to the newly inserted node, or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current, *temp, *new;

	if (head == NULL)
		return (NULL);

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL || number < (*head)->n)
	{
		new->next = *head;
		*head = new;
		return (new);
	}

	current = *head;
	while (current->next != NULL)
	{
		temp = current;
		current = current->next;
		if (current->n > number)
			break;
	}

	if (current->n > number)
	{
		temp->next = new;
		new->next = current;
	}
	else
		current->next = new;

	return (new);
}
