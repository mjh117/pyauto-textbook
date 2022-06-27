from urllib.parse import urljoin

# 현재 디렉터리 결합 --- (1)
# 결과: https://example.com/a/b/tree.jpg
print(urljoin('https://example.com/a/b/c.html', 'tree.jpg'))
print(urljoin('https://example.com/a/b/c.html', './tree.jpg'))

# 한 계층 위 결합 --- (2)
# 결과: https://example.com/a/tree.jpg
print(urljoin('https://example.com/a/b/c.html', '../tree.jpg'))


# 두 계층 위 결합 --- (3)
# 결과: https://example.com/img/tree.jpg
print(urljoin('https://example.com/a/b/c.html','../../img/tree.jpg'))


# 루트 계층 결합 --- (4)
# 결과: https://example.com/tree.jpg
print(urljoin('https://example.com/a/b/c.html', '/tree.jpg'))
