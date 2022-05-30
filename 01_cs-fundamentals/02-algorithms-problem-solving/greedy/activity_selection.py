from typing import List, Tuple

def activity_selection(activities: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Finds the maximum number of non-overlapping activities using the Greedy approach.
    
    The strategy is to always pick the next activity whose finish time is least 
    among the remaining activities and the start time is greater than or equal 
    to the finish time of the previously selected activity.
    
    Args:
        activities: A list of tuples where each tuple (start, end) represents 
                   the start and end time of an activity.
                   
    Returns:
        A list of selected activities (start, end) that are non-overlapping.
        
    Complexity:
        Time: O(n log n) - primarily due to sorting the activities by finish time.
        Space: O(n) - to store the selected activities.
    """
    if not activities:
        return []

    # Sort activities based on their finish times
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected_activities = []
    
    # The first activity always gets selected
    last_finish_time = sorted_activities[0][1]
    selected_activities.append(sorted_activities[0])
    
    for i in range(1, len(sorted_activities)):
        start, finish = sorted_activities[i]
        
        # If the start time is greater than or equal to the finish time of 
        # the last selected activity, then select it
        if start >= last_finish_time:
            selected_activities.append((start, finish))
            last_finish_time = finish
            
    return selected_activities

if __name__ == "__main__":
    # Example usage:
    # Activities (start, finish)
    example_activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11), (8, 12), (2, 13), (12, 14)]
    
    result = activity_selection(example_activities)
    
    print(f"Total activities: {len(example_activities)}")
    print(f"Maximum non-overlapping activities: {len(result)}")
    print("Selected activities:")
    for start, finish in result:
        print(f"  ({start}, {finish})")
