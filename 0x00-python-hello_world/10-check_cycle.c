#include "lists.h"

/**
 * check_cycle - checks if a linked list contains a cycle
 * @list: linked list to check
 * Return: 1 if the list has a cycle, 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *start = list;
	listint_t *last = list;

	if (!list)
		return (0);

	while (start && last && last->next)
	{
		start = start->next;
		last = last->next->next;
		if (start == last)
			return (1);
	}
	return (0);
}
