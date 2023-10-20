#include "lists.h"

/**
 * is_palindrome - check if a linked list is a palindrome.
 * @head: the start of the list.
 *
 * Return: 1 if it's palindrom. otherwise return 0.
 */
int is_palindrome(listint_t **head)
{
	int len = 0;
	int idx = 0;
	int count = 1;
	listint_t *temp;
	listint_t *forward;

	if (*head == NULL)
		return (1);
	temp = *head;
	while (temp != NULL)
	{
		len++;
		temp = temp->next;
	}
	if ((len % 2) != 0)
		return (0);
	if (len == 2)
	{
		if ((*head)->n != (*head)->next->n)
			return (0);
	}
	temp = *head;
	while (count != (len / 2) + 1)
	{
		temp = temp->next;
		count++;
	}
	forward = temp;
	while (forward != NULL)
	{
		if (forward->n != get_curr_back(*head, len, idx)->n)
			return (0);
		forward = forward->next;
		idx++;
	}
	return (1);
}

/**
 * get_curr_back - get current node moving backwards.
 * @head: the start of the list.
 * @len: length of the list.
 * @idx: the index of item from the center.
 *
 * Return: current node moving backward.
 */
listint_t *get_curr_back(listint_t *head, int len, int idx)
{
	int count = 1;
	listint_t *curr_back = head;

	while (count != (len / 2) - idx)
	{
		curr_back = curr_back->next;
		count++;
	}
	return (curr_back);
}
