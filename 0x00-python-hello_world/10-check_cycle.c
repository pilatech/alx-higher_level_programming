#include "lists.h"

/**
 * check_cycle - check if a linked list has a cycle.
 * @list: pointer to the linked list.
 *
 * Return: 0 if no cycle and 1 if there is.
 */
int check_cycle(listint_t *list)
{
	listint_t *temp;

	if (list == NULL)
		return (0);
	temp = list;
	while (temp != NULL)
	{
		if (temp->next == list)
			return (1);
		temp = temp->next;
	}
	return (0);
}
