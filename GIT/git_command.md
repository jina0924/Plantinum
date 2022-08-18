# git 명령어
- 프로젝트의 용이성을 위해 개인적으로 정리한 명령어입니다.

---

## git clone
```
1. 해당 폴더 위치에서 마우스 우클릭 + git bash에서 열기
2. git clone [git REPO_URL] [대상 폴더]
	ex) $ git clone https://lab.ssafy.com/s07-webmobile3-sub2/S07P12A109 S07P12A109
```

## git branch
```
1. 기존에 존재하지 않는 branch를 제작 후 이동 시
> $ git switch -c [브랜치 이름]
2. 기존에 존재하는 branch로 이동 시
> $ git switch [브랜치 이름]
```

## git commit
```
$ git status : git 상태확인
$ git add . : 폴더에 있는 모든 파일 staging
$ git commit -m "[커밋 메세지]" : "" 안에 있는 메세지와 함께 commit
$ git push origin main : 원격 저장소에 push
$ git pull : 내려받기 (*branch를 명확하게 하고 싶다면 git pull origin [branch])
```

## 복사, 붙여넣기
```
$ Shift+Del   : Ctrl+C (~2가 뜨는 건 정상입니다) 
$ Shift+INS   : Ctrl+V
```