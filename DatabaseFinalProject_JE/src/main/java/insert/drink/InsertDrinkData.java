package insert.drink;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Random;

public class InsertDrinkData {
    static final String jdbcDriver = "org.mariadb.jdbc.Driver";
    static final String dbURL = "jdbc:mariadb://140.127.74.170/410877027";
    static final String user = "410877027";
    static final String password = "410877027";
    static Random random = new Random();
    static int temp = 1;

    public static void main(String[] argv) {
        try {
            Class.forName(jdbcDriver);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }
        try {

            Connection connection = DriverManager.getConnection(dbURL, user, password);
            for (temp = 25; temp < 51; temp++)
                createData(
                        connection,
                        temp-25,
                        temp,
                        "飲品" + (temp - 25 ),
                        random.nextInt(3000) + 1,
                        random.nextInt(1000) + 1,
                        random.nextInt(300) + 20
                );

        } catch (SQLException throwable) {
            throwable.printStackTrace();
        }
    }

    private static void createData(Connection connection,
                                   int drink_id,
                                   int commodity_id,
                                   String drink_name,
                                   int drink_amount,
                                   int drink_sale_amount,
                                   int drink_price) throws SQLException {
        PreparedStatement preparedStatement =
                connection.prepareStatement("REPLACE INTO " +
                        "drink(" +
                        "drink_id," +
                        "commodity_id," +
                        "drink_name," +
                        "drink_amount," +
                        "drink_sale_amount," +
                        "drink_price) " +
                        "VALUES (?,?,?,?,?,?)");
        preparedStatement.setInt(1, drink_id);
        preparedStatement.setInt(2, commodity_id);
        preparedStatement.setString(3, drink_name);
        preparedStatement.setInt(4, drink_amount);
        preparedStatement.setInt(5, drink_sale_amount);
        preparedStatement.setInt(6, drink_price);
        preparedStatement.executeUpdate();
    }

}
