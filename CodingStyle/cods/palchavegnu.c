if (condition) {
    do_this();
    do_that();
} else {
    otherwise();
}

switch (action) {
    case KOBJ_ADD:
        return "add";
    case KOBJ_REMOVE:
        return "remove";
    case KOBJ_CHANGE:
        return "change";
    default:
        return NULL;
}

do {
    body of do-loop
} while (condition);
