public class Student {
    public int studentID;
	public String studentName;
	public String address;
	
	//생성자1 구현
	public Student(String name) {
		
		studentName = name;
	}
	
	//생성자2 구현
    public Student(int id, String name) {

    	studentID = id;
    	studentName = name;
    	address = "주소 없음"; // 안쓸시 기본값은 null
    }
	
	public void showStudentInfo(){
		System.out.println(studentName +","+ address);
		
	}
	
	public String getStudentName() {
		
		return studentName;
	}
}
