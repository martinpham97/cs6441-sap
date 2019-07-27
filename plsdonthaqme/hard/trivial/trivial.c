#include <stdio.h>
#include "trivial_allocator.h"

#define MAX_ITEMS 500000

struct node {
    struct node* parent;
    char* name;
    int price;
};

int current_index = 0;
struct node* items[MAX_ITEMS];
struct node** root = HEAP_START; // Pointer to root node

void flush(void) {
	char ch;
	while ((ch = getchar()) && ch != EOF && ch != '\n'){}
}

struct node* create_item() {
    struct node* item = trivial_malloc(sizeof(struct node));
    item->name = trivial_malloc(128);
    
    if (current_index == 0) {
        item->parent = *root;
    } else {
        item->parent = items[current_index - 1];
    }
    memset(item->name, 0, 128);

    printf("Created new item. Id %d\n", current_index);
    items[current_index++] = item;

    return item;
}

void add_item() {
    if (current_index >= MAX_ITEMS) {
        printf("Too many items\n");
        return;
    }
    create_item();
}

void set_name() {
    int item;
    printf("Which item do you want to set the name of: ");
    scanf("%d", &item);
    flush();

    if (item < 0 || item >= current_index) {
        return;
    }
    
    printf("What do you want the name to be: ");
    fgets(items[item]->name, 128, stdin);
}

void set_price() {
    int item;
    printf("Which item do you want to set the name of: ");
    scanf("%d", &item);
    flush();

    if (item < 0 || item >= current_index) {
        return;
    }
    
    printf("What do you want the price to be: ");
    scanf("%ld", &items[item]->price);
}

void print_item() {
    int item;
    printf("Which item do you want to set the name of: ");
    scanf("%d", &item);
    flush();

    if (item < 0 || item >= current_index) {
        return;
    }

    if (items[item]->name == NULL) {
        printf("NULL - %ld\n", items[item]->price);

    } else {
        printf("%s - %ld\n", items[item]->name, items[item]->price);
    }

}


int menu() {
	printf("\n");
	printf("[a]dd item\n");
	printf("[s]et name\n");
	printf("s[e]t price\n");
	printf("[p]rint item\n");
	printf("[q]uit\n");
	printf("\n");
	printf("enter your choice, (or press enter to refresh): ");

	char ch = getchar();
	switch (ch) {
		case EOF:
        case 'q':
		case 'Q':
            exit(0);
			return 0;

        case 'e': 
        case 'E':
            flush();
            set_price();
			break;

 
        case 's': 
        case 'S':
            flush();
            set_name();
			break;

		case 'a': 
        case 'A':
            flush();
			add_item();
			break;

        case 'p':
		case 'P':
			flush();
            print_item();
			break;


		default:
			printf("\n");
			break;
	}

	return 1;
}

int main(void) {
    setbuf(stdout, NULL);
    *root = (struct node*) &root;

    do {
    } while (menu());
}

