#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * check_cycle - checking for cycles
 * @list: head of list
 * Return: 1 when finding a cycle
*/


int check_cycle(listint_t *list)
{
	listint_t *first = list, *secend = list;
	while (first && secend->next)
	{
		first = first->next;
		secend = secend->next->next;
		if (first == secend)
			return (1);
	}

	return (0);
}
