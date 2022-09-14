def solution(id_list, report, k):
    received = {name:set() for name in id_list}
    reported_dict = {name:set() for name in id_list}

    for rp in report:
        frm, to = rp.split()
        reported_dict[to].add(frm)
        if len(reported_dict[to]) >= k:
            for rpt in reported_dict[to]:
                received[rpt].add(to)
    rst = [len(names) for names in received.values()]
    return rst