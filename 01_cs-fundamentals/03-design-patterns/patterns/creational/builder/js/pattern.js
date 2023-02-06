/**
 * SQL Query Builder for SELECT, WHERE, JOIN, LIMIT chaining
 */
class SQLQuery {
    constructor() {
        this.table = "";
        this.fields = ["*"];
        this.wheres = [];
        this.joins = [];
        this.limitNum = null;
    }

    toString() {
        let query = `SELECT ${this.fields.join(", ")} FROM ${this.table}`;
        if (this.joins.length > 0) {
            query += " " + this.joins.join(" ");
        }
        if (this.wheres.length > 0) {
            query += " WHERE " + this.wheres.join(" AND ");
        }
        if (this.limitNum !== null) {
            query += ` LIMIT ${this.limitNum}`;
        }
        return query + ";";
    }
}

class SQLQueryBuilder {
    constructor() {
        this.query = new SQLQuery();
    }

    from(table) {
        this.query.table = table;
        return this;
    }

    select(fields) {
        this.query.fields = Array.isArray(fields) ? fields : [fields];
        return this;
    }

    where(field, operator, value) {
        this.query.wheres.push(`${field} ${operator} '${value}'`);
        return this;
    }

    join(table, on) {
        this.query.joins.push(`JOIN ${table} ON ${on}`);
        return this;
    }

    limit(num) {
        this.query.limitNum = num;
        return this;
    }

    build() {
        return this.query.toString();
    }
}

// Example usage
const query = new SQLQueryBuilder()
    .from("users")
    .select(["id", "name", "email"])
    .join("orders", "users.id = orders.user_id")
    .where("active", "=", "1")
    .limit(10)
    .build();

console.log(query);
