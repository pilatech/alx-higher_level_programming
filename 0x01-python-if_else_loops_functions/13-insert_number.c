#include "lists.h"

/**
 * insert_node - insert a node into sorted list.
 * @head: pointer to the begining of the list.
 * @number: the number to insert.
 *
 * Return: pointer to the modified list.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node;
	listint_t *back;
	listint_t *front;

	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;
	new_node->next = NULL;

	if (*head == NULL)
	{
		*head = new_node;
	}
	else
	{
		back = *head;
		front = (*head)->next;
		while (1)
		{
			if ((back->n <= new_node->n) &&
					(front == NULL || (front->n > new_node->n)))
			{
				new_node->next = front;
				back->next = new_node;
				break;
			}
			else
			{
				new_node->next = back;
				*head = new_node;
				break;
			}
			back = back->next;
			front = front->next;
		}
	}
	return (*head);
}
