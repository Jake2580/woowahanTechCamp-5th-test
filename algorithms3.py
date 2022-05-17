def solution(board):
    answer = 0  # 한 획으로 가장 많이 삭제한 블록 개수
    block_group = dict()  # 근처에 있는 블록끼리 묶기 위한 딕셔너리
    
    ### 블록 그룹에 요소 추가
    for x in range(len(board)):
        for y in range(len(board)):
            coord = (x, y)  # 현재 좌표

            if board[x][y] not in block_group:  # 요소 없음
                block_group[board[x][y]] = [[coord]]
                continue
               
            sw = -1
            # -1: 어느 그룹에도 속하지 못함, n: 해당 알파벳의 n번째 그룹에 속함

            def find_my_block_group(a=0, b=0):
                nonlocal sw
                
                if board[x][y] != board[x+a][y+b]:
                    return
                
                for i in range(len(block_group[board[x][y]])):
                    if (x+a, y+b) in block_group[board[x][y]][i] and sw != i:
                        block_group[board[x][y]][i].append(coord)
                        
                        if -1 < sw:
                            block_group[board[x][y]][sw] = list(set(block_group[board[x][y]][sw] + block_group[board[x][y]][i]))
                            del block_group[board[x][y]][i]
                            break
                        
                        sw = i
                        break
            
            if 0 <= x - 1:  # 위쪽 확인
                find_my_block_group(a=-1)
                            
            if 0 <= y - 1:  # 왼쪽 확인
                find_my_block_group(b=-1)
                        
            if y + 1 < len(board):  # 오른쪽 확인
                find_my_block_group(b=1)
                            
            if sw == -1:  # 새그룹 생성
                block_group[board[x][y]].append([coord])
                
    ### 최대로 많이 삭제한 블록 수 찾기
    def delete_block(x, y, delete_blocks):
        coord = (x, y)
        
        for i in range(len(block_group[board[x][y]])):
            if coord in delete_blocks:
                continue
            
            if coord in block_group[board[x][y]][i]:
                delete_blocks += block_group[board[x][y]][i]
                break
            
        return delete_blocks
    
    for x in range(len(board)):  
        delete_blocks = [[], []]  # 행, 열을 한번에 진행하기 위한 이차원 리스트
        
        for y in range(len(board)):
            delete_blocks[0] = delete_block(x, y, delete_blocks[0])  # 열
            delete_blocks[1] = delete_block(y, x, delete_blocks[1])  # 행
                    
        if len(delete_blocks[0]) < len(delete_blocks[1]):
            max_delete_blocks = len(delete_blocks[1])
        else:
            max_delete_blocks = len(delete_blocks[0])
                    
        if answer < max_delete_blocks:
            answer = max_delete_blocks
            
            # 최대로 나올 수 있는 블록들을 다 지웠다면 break
            if answer == len(board) ** 2:
                break
    
    return answer
