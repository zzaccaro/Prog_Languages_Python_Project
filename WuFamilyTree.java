import java.util.Scanner;
import java.io.*;
import java.util.StringTokenizer;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Iterator;
import java.util.Map;
import java.util.Collections;

public class WuFamilyTree {

    private static HashMap<String,Person> familyGraph = new HashMap<String, Person>();

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String line = "";
        StringTokenizer tokenizer;
        String method, arg1, arg2, arg3;

        while (in.hasNextLine()) {
            line = in.nextLine();
            tokenizer = new StringTokenizer(line, " ");
            method = tokenizer.nextToken();
            arg1 = tokenizer.nextToken().toLowerCase();
            arg2 = tokenizer.nextToken().toLowerCase();

            try {
                arg3 = tokenizer.nextToken().toLowerCase();
            } catch (java.util.NoSuchElementException e){
                arg3 = "";
            }

            switch(method) {
            case "E":
                E(arg1, arg2, arg3);
                break;
            case "R":
                System.out.println("R " + arg1 + " " + arg2);
                System.out.println(R(arg1, arg2));
                System.out.println();
                break;
            case "W":
                System.out.println("W " + arg1 + " " + arg2);
                ArrayList<String> people = new ArrayList<String>();
                people = W(arg1, arg2);
                for (String person: people)
                    {
                        System.out.println(person);
                    }
                System.out.println();
                break;
            case "X":
                System.out.println("X " + arg1 + " " + arg2 + " " + arg3);
                System.out.println(X(arg1, arg2, arg3));
                System.out.println();
                break;
            }
        }
    }

    private static void E(String name1, String name2, String name3) {
        checkOrAddToGraph(name1, name1, name1);
        checkOrAddToGraph(name2, name2, name2);
        checkOrAddToGraph(name3, name1, name2);

        familyGraph.get(name1).addSpouse(name2);
        familyGraph.get(name2).addSpouse(name1);
    }

    private static void checkOrAddToGraph(String nodeName, String parent1, String parent2) {
        boolean existsInGraph = familyGraph.containsKey(nodeName);
        if(existsInGraph == false) {
            familyGraph.put(nodeName, new Person(nodeName, parent1, parent2));
        } else if (isAdamAndEve(nodeName) == true) {
            familyGraph.get(nodeName).setParents(parent1, parent2);
        }
        if (!parent1.equals(parent2)) {
            familyGraph.get(parent1).setChildren(nodeName);
            familyGraph.get(parent2).setChildren(nodeName);
        }
    }

    private static boolean isAdamAndEve(String name) {
        if(familyGraph.get(name).getParents().contains(name)) {
            return true;
        }
        return false;
    }

    private static String R(String name1, String name2) {
        Person person1 = familyGraph.get(name1);
        Person person2 = familyGraph.get(name2);
        if (person1 == null || person2 == null) {
            return "unrelated";
        }
        else if(isSpouse(person1, person2)) {
            return "spouse";
        }
        else if(isParent(person1, person2)) {
            return "parent";
        }
        else if(isSibling(person1, person2)) {
            return "sibling";
        }
        else if(isAncestor(person1, person2)) {
            return "ancestor";
        }
        else if(isRelative(person1, person2)) {
            ArrayList<String> ancestors = getAncestors(person1);
            return "relative";
        }
        return "unrelated";
    }

    private static boolean isSpouse(Person person1, Person person2) {
        return person1.getSpouse().contains(person2.getName());
    }

    private static boolean isParent(Person person1, Person person2) {
        if(person1.getName().equals(person2.getName())) {
            return false;
        }
        if(person2.getParents().contains(person1.getName())) {
            return true;
        }
        return false;
    }

    private static boolean isSibling(Person person1, Person person2) {
        if(isAdamAndEve(person1.getName()) || isAdamAndEve(person1.getName())) {
            return false;
        }
        ArrayList<String> person1Parents = person1.getParents();
        ArrayList<String> person2Parents = person2.getParents();
        Collections.sort(person1Parents);
        Collections.sort(person2Parents);
        return person1Parents.equals(person2Parents);
    }

    private static boolean isAncestor(Person p1, Person p2) {
        if (p1.getName().equals(p2.getName()) && isAdamAndEve(p1.getName()))
            {
                return true;
            }
        if (checkParents(p1, p2))
            return true;
        else
            return false;
    }

    private static boolean checkParents(Person target, Person p) {
        if(isAdamAndEve(p.getName())) {
            return false;
        }
        else if(p.getParents().get(0).equalsIgnoreCase(target.getName())) {
            return true;
        }
        else if(p.getParents().get(1).equalsIgnoreCase(target.getName())) {
            return true;
        }
        else if(checkParents(target, familyGraph.get(p.getParents().get(0)))){
            return true;
        }
        else if(checkParents(target, familyGraph.get(p.getParents().get(1)))){
            return true;
        }
        else {
            return false;
        }
    }

    private static boolean isRelative(Person p1, Person p2) {
        ArrayList<String> p1Relatives = getAncestors(p1);
        ArrayList<String> p2Relatives = getAncestors(p2);
        for(String person1 : p1Relatives) {
            for (String person2 : p2Relatives) {
                if(person1.equals(person2)) {
                    return true;
                }
            }
        }
        return false;
    }

    private static String X(String name1, String relation, String name2) {
        Person person1 = familyGraph.get(name1);
        Person person2 = familyGraph.get(name2);
        if (person1 == null || person2 == null) {
            return "No";
        }

        String answer = "";
        switch(relation)
            {
            case "spouse":
                answer = (isSpouse(person1, person2) ? "Yes" : "No");
                break;
            case "parent":
                answer = (isParent(person1, person2) ? "Yes" : "No");
                break;
            case "sibling":
                answer = (isSibling(person1, person2) ? "Yes" : "No");
                break;
            case "ancestor":
                answer = (isAncestor(person1, person2) ? "Yes" : "No");
                break;
            case "relative":
                answer = (isRelative(person1, person2) ? "Yes" : "No");
                break;
            case "unrelated":
                answer = (!isRelative(person1, person2) ? "Yes" : "No");
                break;
            }
        return answer;
    }

    private static ArrayList<String> W(String relation, String name) {

        Person p = familyGraph.get(name);
        ArrayList<String> people = new ArrayList<String>();
        switch(relation)
            {
            case "spouse":
                people.addAll(p.getSpouse());
                break;
            case "parent":
                if (isAdamAndEve(p.getName()))
                    people.add(p.getName());
                else
                    people.addAll(p.getParents());
                break;
            case "sibling":
                people.addAll(getSiblings(p));
                break;
            case "ancestor":
                people.addAll(getAncestors(p));
                break;
            case "relative":
                people.addAll(getRelatives(p));
                break;
            case "unrelated":
                people.addAll(getStrangers(p));
                break;
            }
        Collections.sort(people);
        return people;
    }

    private static ArrayList<String> getSiblings(Person p)
    {
        ArrayList<String> siblings = new ArrayList<String>();
        for(Map.Entry<String, Person> entry : familyGraph.entrySet())
            {
                if (isSibling(p, entry.getValue()))
                    siblings.add(entry.getKey());
            }
        return siblings;
    }

    private static ArrayList<String> getAncestors(Person p) {
        ArrayList<String> ancestors = new ArrayList<String>();
        for(Map.Entry<String, Person> entry : familyGraph.entrySet())
            {
                if (checkParents(entry.getValue(), p))
                    ancestors.add(entry.getKey());
            }
        if(ancestors.size() == 0) {
            ancestors.add(p.getName());
        }
        return ancestors;
    }

    private static ArrayList<String> getRelatives(Person p) {
        ArrayList<String> relatives = new ArrayList<String>();
        for(Map.Entry<String, Person> entry : familyGraph.entrySet())
            {
                if (isRelative(entry.getValue(), p))
                    relatives.add(entry.getKey());
            }
        return relatives;
    }

    private static ArrayList<String> getStrangers(Person p) {
        ArrayList<String> strangers = new ArrayList<String>();
        for(Map.Entry<String, Person> entry : familyGraph.entrySet())
            {
                if (!isRelative(entry.getValue(), p) && !isSpouse(entry.getValue(), p))
                    strangers.add(entry.getKey());
            }
        return strangers;
    }
}