# Sleep sort

Sleep sort works by starting a separate task for each item to be sorted, where each task sleeps for an interval corresponding to the item's sort key, then emits the item. Items are then collected sequentially in time. 
