#include <stdio.h>
#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - The pointer to the new node
 * @head: The pointer to the head
 * @number: the number to be inserted
 * Return: Return the pointer to the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

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

	while (current->next != NULL && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;
	return (new);
}
