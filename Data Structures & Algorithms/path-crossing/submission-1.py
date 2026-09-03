class Solution:
    def isPathCrossing(self, path: str) -> bool:
        # נקודת ההתחלה
        x, y = 0, 0
        
        # מכניסים ל-set את נקודת ההתחלה כ-Tuple
        seen = {(0, 0)}
        
        for direction in path:
            # עדכון המיקום לפי הכיוון
            if direction == 'N':
                y += 1
            elif direction == 'S':
                y -= 1
            elif direction == 'E':
                x += 1
            elif direction == 'W':
                x -= 1
                
            # אם הגענו למיקום שכבר שמור לנו - הנתיב נחתך!
            if (x, y) in seen:
                return True
            
            # אם לא, נוסיף את המיקום החדש לזיכרון
            seen.add((x, y))
            
        return False