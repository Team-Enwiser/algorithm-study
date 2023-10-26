public class StudentTest {
    public static void main(String[] args) {

		Student studentLee = new Student("이순신"); //생성자1 사용
		//studentLee.studentName ="이순신";
		studentLee.address = "서울";
		
		studentLee.showStudentInfo();//결과값  이순신,서울
		
		Student studentKim = new Student(1234,"김유신"); //생성자2 사용
		//studentKim.studentName ="김유신";
		//studentKim.address = "경주";
		
		studentKim.showStudentInfo();//결과값 김유신,주소 없음
	
	}
}
