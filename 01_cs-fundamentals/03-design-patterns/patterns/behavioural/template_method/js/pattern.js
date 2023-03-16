/**
 * Template Method pattern implementation for a Report Generator
 * ES2022 Node.js environment
 */

class ReportGenerator {
  /**
   * The template method defining the algorithm skeleton.
   */
  generate() {
    console.log(`\n--- Generating ${this.constructor.name} ---`);
    this.generateHeader();
    this.generateBody();
    this.generateFooter();
    console.log("--- Generation Finished ---");
  }

  generateHeader() {
    console.log("Header: Standard Report Header");
  }

  // Primitive operations to be implemented by subclasses
  generateBody() {
    throw new Error("Method generateBody() must be implemented.");
  }

  generateFooter() {
    console.log("Footer: Standard Page 1 / 1");
  }
}

class HTMLReportGenerator extends ReportGenerator {
  generateHeader() {
    console.log("Header: <html><head><title>HTML Report</title></head><body>");
  }

  generateBody() {
    console.log("Body: <div><h1>Data Summary</h1><p>Sales are up by 20%.</p></div>");
  }

  generateFooter() {
    console.log("Footer: </body></html>");
  }
}

class PDFReportGenerator extends ReportGenerator {
  generateBody() {
    console.log("Body: [PDF Content] - Table of transactions, Charts, and Metrics.");
  }

  generateFooter() {
    console.log(`Footer: PDF ID: ${Math.random().toString(36).substring(7)}`);
  }
}

// Client Code
const htmlGen = new HTMLReportGenerator();
htmlGen.generate();

const pdfGen = new PDFReportGenerator();
pdfGen.generate();
