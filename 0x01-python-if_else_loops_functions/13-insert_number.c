#include "lists.h"

/**
 * insert_node - inserts a number into a sorted singly linked
 * @head: head pointer to a linked list
 * @number: the number to insert
 * Return: the address of the new node, or NULL if it failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *node = *head;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (node == NULL || node->n >= number)
	{
		new->next = node;
		*head = new;
		return (new);
	}

	if (*head != NULL)
	{
		new = (*head)->next;
		new->n = number;
		new->next = NULL;
	}
	while (node && node->next && node->next->n < number)
	{
		node = node->next;
	}
	new->next = node->next;
	node->next = new;

	return (new);

}
