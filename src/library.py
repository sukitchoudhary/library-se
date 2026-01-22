    def generate_report(self):
        report = ["ID | Title | Author | Status"]
        for book_id, data in self.books.items():
            report.append(
                f"{book_id} | {data['title']} | {data['author']} | {data['status']}"
            )
        return "\n".join(report)
