def build_tree(items):
    item_map = {item.id: item for item in items}
    tree = []
    for item in items:
        item.children_list = []
        if item.parent_id:
            parent = item_map[item.parent_id]
            parent.children_list.append(item)
        else:
            tree.append(item)
    return tree


def get_active_branch(path, items):
    url_map = {item.get_url(): item for item in items}
    active = url_map.get(path)
    branch = set()
    while active:
        branch.add(active.id)
        active = active.parent
    return branch