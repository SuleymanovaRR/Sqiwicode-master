l = login[1:]
    s = requests.Session()
    header = {'Content-type': 'application/json',
              'X-Requested-With': 'XMLHttpRequest',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
              }
    s.headers = header
    r = s.post('https://auth.qiwi.com/cas/tgts', json={'login': login, 'password': password})
    tgt_ticket = json.loads(r.text)['entity']['ticket']
    header = {'Content-type': 'application/json',
              'Accept': 'application/vnd.qiwi.sso-v1+json',
              'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
              }
    s.headers = header
    r = s.post('https://auth.qiwi.com/cas/sts',
               json={'service': 'https://qiwi.com/j_spring_cas_security_check', 'ticket': tgt_ticket})
    st_ticket = json.loads(r.text)['entity']['ticket']
    r = s.get('https://qiwi.com/j_spring_cas_security_check?ticket=' + st_ticket)
    cookies = r.cookies
    r = s.post('https://auth.qiwi.com/cas/sts',
               json={'service': 'http://t.qiwi.com/j_spring_cas_security_check', 'ticket': tgt_ticket}, cookies=cookies)
    st_ticket_2 = json.loads(r.text)['entity']['ticket']
    s.headers = {'Accept': 'application/json', 'Authorization': 'Token ' + st_ticket_2,
                 'Content-type': 'application/json'}
    p = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + l + '/payments?rows=50', cookies=cookies)
    payments = json.loads(p.text)['data']