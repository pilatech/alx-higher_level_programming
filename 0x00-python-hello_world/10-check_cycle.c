#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle.
 * @list: pointer to the linked list.
 *
 * Return: 0 if no cycle and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *first = list;

	while (list != NULL)
	{
		list = list->next;
		if (list == first)
			return (1);
	}
	return (0);
}
