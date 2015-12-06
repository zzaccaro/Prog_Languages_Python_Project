import java.util.ArrayList;

public class Person implements Comparable<Person>
{
	String name;
	ArrayList<String> parents;
    ArrayList<String> spouse;
    ArrayList<String> children;
    ArrayList<String> ancestors;

	public Person(String n)
	{
		name = n;
		parents = new ArrayList<String>();
		spouse = new ArrayList<String>();
    children = new ArrayList<String>();
    ancestors = new ArrayList<String>();
	}

    public Person(String n, String parent1, String parent2)
	{
		name = n;
		parents = new ArrayList<String>();
    parents.add(parent1);
    parents.add(parent2);
		spouse = new ArrayList<String>();
    children = new ArrayList<String>();
    ancestors = new ArrayList<String>();
	}
	
	public String getName()
	{
		return name;
	}
	
	public ArrayList<String> getParents()
	{
		return parents;
	}
	
	public ArrayList<String> getSpouse()
	{
		return spouse;
	}

	public void addParent(String n)
	{
		parents.add(n);
	}

    public void setParents(String parent1, String parent2)
    {
        parents.clear();
        parents.add(parent1);
        parents.add(parent2);
        
    }

    public void setChildren(String childName)
    {
        children.add(childName);
    }

    public ArrayList<String> getChildren()
    {
        return children;
    }

	public void removeParent(String n)
	{
		parents.remove(n);
	}

	public void addSpouse(String n)
	{
      if(!spouse.contains(n)) {
          spouse.add(n);
      }
	}
	
	public int compareTo(Person other) {
	    String name1 = this.name.toLowerCase();
	    String name2 = other.getName().toLowerCase();
	    
	    if (name1.equals(name2))
	    	return 0;
	    else
	    	return 1;
	}

    public String toString() {
        return("Name: " + name + "\n" +
               "Parents: " + parents + "\n" +
               "Spouses: " + spouse + "\n" +
               "Children: " + children + "\n");
    }

}