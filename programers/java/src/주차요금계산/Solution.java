package 주차요금계산;

import java.util.*;
import java.util.stream.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int defaultTime = fees[0];
        int defaultFee = fees[1];
        int unitTime = fees[2];
        int unitFee = fees[3];

        Map<String, Car> carNumMap = new HashMap<>();

        for (String record : records) {
            int time = 60 * Integer.parseInt(record.substring(0,2)) + Integer.parseInt(record.substring(3, 5));
            String carNum = record.substring(6, 10);
            String status = record.substring(11);
            if (status.equals("IN")) {
                if (!carNumMap.containsKey(carNum)) {
                    carNumMap.put(carNum, new Car(time));
                } else { // 한번 들어왔던 녀석이라면
                    Car car = carNumMap.get(carNum);
                    car.setInTime(time);
                }
            } else {
                Car car = carNumMap.get(carNum);
                car.setOutTime(time);
            }
        }
        List<String> keyList = new ArrayList<>(carNumMap.keySet());
        keyList.sort((i1, i2) -> i1.compareTo(i2));
        List<Integer> answer = new ArrayList<>();
        for (String key : keyList) {
            Car car = carNumMap.get(key);
            int totalTime = car.getTotalTime();
            if (totalTime >= defaultTime) {
                int fee = (int) (defaultFee + Math.ceil((totalTime - defaultTime) / (double) unitTime) * unitFee);
                answer.add(fee);
                continue;
            }
            answer.add(defaultFee);
        }
        return answer.stream().mapToInt(i -> i).toArray();
    }

    static class Car {
        int inTime;
        int outTime = 23 * 60 + 59;
        int totalTime = 0;

        public Car(int inTime) {
            this.inTime = inTime;
            this.totalTime = calcTotalTime();
        }

        public void setOutTime(int outTime) {
            this.outTime = outTime;
            this.totalTime = calcTotalTime();
        }

        public void setInTime(int inTime) {
            // 새롭게 인타입을 정한다면 기존의 토탈타입을 정하고 거기에 새롭게 디폴트로 더해나가야 한다.
            this.inTime = inTime;
            this.outTime = 23 * 60 + 59;
            this.totalTime = totalTime + calcTotalTime();
        }

        public int getTotalTime() {
            return totalTime;
        }

        public int calcTotalTime() {
            return outTime - inTime;
        }

        @Override
        public String toString() {
            return "{" + "inTime: " + inTime + ", outTime: " +outTime + ", totalTime: " + totalTime + "}";
        }
    }
}

class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        int[] fees = {180, 5000, 10, 600};
        String[] records = {"05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"};
        System.out.println(sol.solution(fees, records));
    }
}