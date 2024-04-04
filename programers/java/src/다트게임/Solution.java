package 다트게임;

import java.util.*;

class Solution {
    public int solution(String dartResult) {
        List<Integer> answer = new ArrayList<>();
        List<Integer> bonusIdxs = new ArrayList<>();
        // 정수가 잇는 위치의 모든 점의 인덱스를 찾는다. 아 잠시 점수가 10점 일수 있잖아
        for (int i = 0; i < dartResult.length(); i++) {
            char c = dartResult.charAt(i);
            if (c == 'S' || c == 'D' || c == 'T') bonusIdxs.add(i);
        }
        for (int i = 0; i < bonusIdxs.size() ; i++) {
            int bonusIdx = bonusIdxs.get(i);
            int score = Integer.parseInt(dartResult.substring(i > 0 ? bonusIdxs.get(i - 1) +1 : 0 , bonusIdx));
            if (dartResult.charAt(bonusIdx) == 'D') {
                score = (int) Math.pow(score, 2);
            } else if (dartResult.charAt(bonusIdx) == 'T') {
                score = (int) Math.pow(score, 3);
            }
            if (bonusIdx + 1 < dartResult.length() && (dartResult.charAt(bonusIdx + 1) == '*' || dartResult.charAt(bonusIdx + 1) == '#')) {
                if (dartResult.charAt(bonusIdx) == '*') {
                    if (i > 0) {
                        answer.set(i - 1, answer.get(i - 1) * 2);
                    }
                    score *= 2;
                } else {
                    score *= -1;
                }
            }
            answer.add(score);
        }
        return answer.stream().reduce(0, Integer::sum);
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        String dartResult = "1S2D*3T";
        System.out.println(sol.solution(dartResult));
    }
}