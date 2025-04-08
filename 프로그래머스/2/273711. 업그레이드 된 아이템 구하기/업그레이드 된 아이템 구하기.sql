SELECT ITEM_ID, ITEM_NAME, RARITY
FROM ITEM_INFO
WHERE ITEM_ID IN (SELECT A.ITEM_ID
                  FROM ITEM_INFO I, ITEM_TREE A
                WHERE I.ITEM_ID = A.PARENT_ITEM_ID AND I.RARITY = 'RARE')
ORDER BY ITEM_ID DESC