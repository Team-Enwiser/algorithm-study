public interface Car {
	String carList();
}

class TCar implements Car {
    public String carName;
    public String carManufacturingCompany;
    public int carReleaseYear;
    public int carPrice;
	
	public TCar(String name, String company, int year, int price) {
		carName = name;
        carManufacturingCompany = company;
        carReleaseYear = year;
        carPrice = price;
	}
	
	public String carList() {
		String result = "{" + carName + "}, " + "{" + carManufacturingCompany + "}, " + "{" + carReleaseYear + "}, " + "{" + carPrice + "}";
        // System.out.println(result);
		return result;
	}
}
