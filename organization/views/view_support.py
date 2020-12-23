def historical_changes(history):
    changes = []
    if history is not None :
        last = history.first()
        for all_changes in range(history.count()):
            new_record, old_record = last, last.prev_record
            if old_record is not None:
                delta = new_record.diff_against(old_record)
                changes.append(delta)
            last = old_record
    return changes